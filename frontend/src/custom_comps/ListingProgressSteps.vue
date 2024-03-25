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
                <small :class = "{'text-yellow-600' : items[1].status == false, 'text-red-500': items[1].status == 'deny'}">{{ items[1].small }}</small>
                <Button class = "feedback-display-btn step-btn" text raised v-if = "items[1].status == 'deny'" @click = "displayFeedback">See Feedback</Button>
            </div>
            <Dialog v-model:visible="feedbackDialogVisible" modal header="Admin's feedback" :style="{ width: '25rem' }">
                <div class="flex align-items-center gap-3 mb-3">
                    {{ feedbackText }}
                </div>
            </Dialog>

            <div class = "step-title-box flex flex-column align-items-center">
                Listing Finalized
                <small :class = "{'text-yellow-600' : items[2].status == false}">{{ items[2].small }}</small>
                <Button class = "step-btn" text raised v-if = "items[2].status" @click = "toListingDetails">Listing Details</Button>
            </div> 
        </div>
    </div>
</template>

<script>
import Steps from 'primevue/steps'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import axios from 'axios'
export default {
    props: {product: Object, adminApproval: String, productId: String },
    components: { Dialog, Steps, Button },
    data(){
        return {
            completedIcon: 'pi pi-check',
            completeTheme: 'bg-primary',
            items: [
                {icon: 'pi pi-upload', status: true, small: 'Completed'}, 
                {icon: 'pi pi-users', status: false, small: 'Pending'}, 
                {icon: 'pi pi-check-square', status: false, small: 'Pending'}
            ],
            feedbackDialogVisible: false,
            feedbackText: '',
        }
    },
    created(){
        if(this.adminApproval == "True"){
            this.items[1].status = 'true'
            this.items[2].status = 'true'
            this.items[1].small= 'Completed'
            this.items[2].small= 'Completed'
        }

        if(this.adminApproval == "Deny"){
            this.items[1].status = 'deny'
            this.items[1].small= 'Denied'
        }
    },

    methods:{
        displayFeedback(){
            axios.get(`http://localhost:8000/admin_actions/get_negative_feedback/${this.productId}`)
            .then(response => {
                console.log(response)
                this.feedbackText = response.data.feedback
            })
            .catch(error => console.log(error))
            this.feedbackDialogVisible = true
            console.log(this.feedbackDialogVisible)
        },

        toListingDetails(){
        },

        toListingPreview(){
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