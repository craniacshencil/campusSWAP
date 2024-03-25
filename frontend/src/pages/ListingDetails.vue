<template>
<Toast />
<div class="void">
    <pageHeader />
    <pageNav />
    <div v-if = "infoReached" class="product-basics flex justify-content-between flex-wrap">
        <Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px"
        :showThumbnails="false" :showIndicators="true" :changeItemOnIndicatorHover="true" :showIndicatorsOnItem="inside"
        :circular="true" :showItemNavigators="true">
            <template #item="slotProps">
                <img :src="slotProps.item.itemImageSrc" alt="No Image" style="width: 100%" />
            </template>
        </Galleria>

        <div class="product-details">
            <h1 class = "product-title">{{ productInfo.title }}</h1>
            <h2 class = "price">₹{{ productInfo.price }}</h2>
            <p>Condition of the item: {{ productInfo.selectedCondition }}</p>
            <p>Product Description: {{ productInfo.productDesc }}</p>
            <div v-if = "fromAdmin">
                <p>category: {{ productInfo.category}}</p>
                <p>Selected Year: {{ productInfo.selectedYear }}</p>
                <p>Selected Branch: {{ productInfo.selectedBranch }}</p>
                <p>Selected Item Type: {{ productInfo.selectedItemType }}</p>
                <p>Selected Conditon: {{ productInfo.selectedCondition }}</p>
            </div>
            <Button icon = "pi pi-phone" label = "Contact Seller" severity = "contrast" raised />
            <Button icon = "pi pi-heart" label= "Wishlist" severity = "secondary" raised />

            <Button v-if = "!fromMyListings && !fromAdmin" @click = "confirmListing" label = "Confirm Listing" class = "confirm-btn" raised />
            <Button v-if = "fromAdmin" @click = "grantApproval" label = "Grant Approval" class = "confirm-btn" raised />
            <Button v-if = "fromAdmin" @click = "denyApproval" label = "Deny Approval" class = "confirm-btn" raised />
            <div class="feedback-denied-section" v-if = "showFeedbackTextArea">
                <FloatLabel>
                    <Textarea autoResize rows = "8" class = "feedback-text-area" v-model="denialFeedback" required/>
                    <label for="feedback-text-area">Feedback for Denial</label>
                </FloatLabel>
                <Button @click = "sendFeedback" label = "Submit Feedback" class = "confirm-btn" raised/>
            </div>
        </div>
    </div>
    <!-- Temporary fix for if you try to access url without filling sell form -->
    <div v-if = "!infoReached" class="product-basics flex justify-content-between"> 
        <div>
            <Skeleton width = "50rem" height = "30rem" class="mb-2"></Skeleton>
        </div>
        <div class = "flex flex-column gap-3">
            <Skeleton width="30rem" height = "2rem" class="mb-2"></Skeleton>
            <Skeleton width="10rem" height = "1.5rem" class="mb-2"></Skeleton>
            <Skeleton width = "20rem" height="1rem" class="mb-2"></Skeleton>
            <Skeleton width="20rem" height="1rem" />
            <div class = "btn-section flex gap-2">
                <Skeleton width="10rem" height="2rem" />
                <Skeleton width="10rem" height="2rem" />
            </div>
        </div>
    </div>
    <!-- <Button v-if = "productListed" @click = "this.$router.push({name: 'Settings'})" label = "Redirect" class = "contrast confirm-btn" raised /> -->
</div>

</template>
<script>
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import pageNav from '@/custom_comps/pageNav.vue';
import pageHeader from '@/custom_comps/pageHeader.vue';
import Galleria from 'primevue/galleria';
import Skeleton from 'primevue/skeleton';
import axios from 'axios'
import Textarea from 'primevue/textarea';
import FloatLabel from 'primevue/floatlabel';
export default{
    data(){
        return{
            infoReached: false,
            prouductInfo: null,
            images: [],
            fromMyListings: false,
            fromAdmin: false,
            showFeedbackTextArea: false,
            denialFeedback: '',
        }
    },
    components: { Textarea, FloatLabel, Toast, Skeleton, Button, pageNav, pageHeader, Galleria },
    methods: {
        //This function will be activated on 'Listing preview' when user first lists their product
        confirmListing(){
            axios.post("http://localhost:8000/products/sell_form", this.productInfo) 
            .then(response => {
                this.$toast.add({ severity: 'success', summary: 'Successfully Listed', detail: `Redirecting...`, life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Settings'})}, 3000)
            })
            .catch(error => console.log("Form data could not be sent"))
        },

        //This function is activated on 'Inspect Listing' by admin if they have no problem with the listing
        grantApproval(){
            console.log(this.productInfo)
            const productIdJSON = {
               productId: this.$route.params.productId
            }
            axios.post("http://localhost:8000/admin_actions/grant_approval", productIdJSON)
            .then(response => {
                this.$toast.add({ severity: 'success', summary: 'Admin Approval Granted!', detail: 'Redirecting to dashboard', life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Admin Dashboard'})}, 3000)
            }
                )
            .catch(error => console.log(error))
        },

        denyApproval(){
            this.showFeedbackTextArea = true
        },

        sendFeedback(){
            console.log(this.denialFeedback)
            const feedbackJSON = {
                productId: this.$route.params.productId,
                feedback: this.denialFeedback,
            }
            console.log(feedbackJSON)
            axios.post("http://localhost:8000/admin_actions/send_negative_feedback", feedbackJSON)
            .then(response => console.log(response))
            .catch(error => console.log(error))
        }

    },
    created(){
        //storing product info in local variable
        console.log(this.$route.params)
        this.productInfo = JSON.parse(this.$route.params.product)
        //Galleria requires a list of JSONs to display images, therefore creating this
        for(let url of this.productInfo.image_urls)
            this.images.push({itemImageSrc: url, alt: "No Image Available"})
        //To Not dispaly 'Confirm Listing' button when you are coming here from the 'MyListings' panel from 'Settings page'
        if(this.$route.params.fromMyListing)
            this.fromMyListings = true
        //To display specific thing that will only be seen on admin page
        if(this.$route.params.fromAdmin)
            this.fromAdmin = true
        this.infoReached = true
    }
}
</script>

<style>
.void{
    background-color: #09090b;
    height: 100%;
    width: 100%;
    
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
}

.product-details .product-basics{
    width: 90%;
}

.product-details{
    width: 40%;
}

.product-details .product-title{
    margin: 0;
}

.product-details .price{
    margin: 0;
}

.product-details .confirm-btn{
    border-radius: 0;
}

.product-details .btn-section{
    margin-top: 5rem;
}

.product-details .p-inputtextarea.p-inputtext{
    width: 80%;
}
</style>
