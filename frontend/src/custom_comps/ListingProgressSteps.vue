<template>
    <div class="steps-main-wrapper flex flex-column">
        <Steps :model="items" :readonly="true">
            <template #item="{ item, active }">
                <div class="inline-flex align-items-center justify-content-center align-items-center border-circle border-primary border-1  h-3rem w-3rem z-1 cursor-pointer" :class = '{ "bg-primary" : item.status, "text-primary surface-overlay" : !item.status }'>
                    <i :class="[item.icon, 'text-xl']" />
                </div>
            </template>
        </Steps>
        <div class="step-titles flex justify-content-around">
            <div class = "step-title-box flex flex-column align-items-center">
                Listing Uploaded 
                <small>{{ items[0].small }}</small>
                <Button text raised class = "step-btn" v-if = "!items[2].status" @click = "toListingPreview">Preview Listing</Button>
            </div>
            <div class = "step-title-box flex flex-column align-items-center">
                Admin Approval
                <small :class = "{'text-red-500' : items[1].status == false}">{{ items[1].small }}</small>
            </div>
            <div class = "step-title-box flex flex-column align-items-center">
                Listing Finalized
                <small :class = "{'text-red-500' : items[2].status == false}">{{ items[2].small }}</small>
                <Button class = "step-btn" text raised v-if = "items[2].status" @click = "toListingDetails">Listing Details</Button>
            </div> 
        </div>
    </div>
</template>

<script>
import Steps from 'primevue/steps'
import Button from 'primevue/button'
export default {
    props: {product: Object, adminApproval: String},
    components: { Steps, Button },
    data(){
        return {
            completedIcon: 'pi pi-check',
            completeTheme: 'bg-primary',
            items: [
                {icon: 'pi pi-upload', status: true, small: 'Completed'}, 
                {icon: 'pi pi-users', status: false, small: 'Pending'}, 
                {icon: 'pi pi-check-square', status: false, small: 'Pending'}
            ],
        }
    },
    created(){
        if(this.adminApproval == 'true'){
            this.items[1].status = 'true'
            this.items[2].status = 'true'
            this.items[1].small= 'Completed'
            this.items[2].small= 'Completed'
        }
    },

    methods:{
        toListingDetails(){
        },

        toListingPreview(){
            console.log("Hello There")
            //WatchMojo: Top 10 reasons why you should learn regex
            const image_url =  this.product.image_urls.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', "").split(",")
            const sessionInfo = JSON.parse(sessionStorage.user)
            this.$router.push({ name: "Listing details", params: {
                product: JSON.stringify({
                    moodleID: sessionInfo.user.moodleID,
                    title: this.product.title,
                    category: this.product.category,
                    price: this.product.price,
                    selectedYear: this.product.selected_year,
                    selectedBranch: this.product.selected_branch,
                    selectedItemType: this.product.selected_item_type,
                    selectedCondition: this.product.selected_condition,
                    productDesc: this.product.product_description,
                    image_urls: image_url, 
                    adminApproval: false,
                }),
                fromMyListing: true,
            }})
        },
    },

    created(){
        console.log(this.product);
    }
}
</script>

<style>
.step-title-box small{
    color: green;
    margin: 0.2rem 0rem;
    /* margin-right: 0.5rem; */
    text-align: center;
}

.step-title-button{
    margin-top: 0.5rem;
}
.p-steps-list{
    height: 10vh;
}

</style>