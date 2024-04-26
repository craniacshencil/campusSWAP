<template>
<Toast />
<div class="void">
    <pageHeader />
    <pageNav />
    <div v-if = "infoReached" class="product-basics pl-8 pt-5 flex flex-wrap justify-content-start gap-8 align-self-start w-full">
        <Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px"
        :showThumbnails="false" :showIndicators="true" :changeItemOnIndicatorHover="true" :showIndicatorsOnItem="inside"
        :circular="true" :showItemNavigators="true">
            <template #item="slotProps">
                <img :src="slotProps.item.itemImageSrc" alt="No Image" style="width: 100%" />
            </template>
        </Galleria>

        <div class="product-details flex-1 pr-8">
            <h1 class = "product-title">{{ productInfo.title }}</h1>
            <h2 class = "price">₹{{ productInfo.price }}</h2>
            <p class = "product-description">{{ productInfo.productDesc }}</p>
            <p class = "product-text-detail">- Condition of the item: {{ productInfo.selectedCondition }}</p>
            <p class = "product-text-detail">- Category: {{ productInfo.category}}</p>
            <p class = "chip-items">- Category of Item:</p>
            <Chip v-for="itemType in productInfo.selectedItemType" :key = "itemType" :label = "itemType" class = "m-0 mr-2" />
            <p class = "chip-items">- Useful for Year:</p>
            <Chip v-for="year in productInfo.selectedYear" :key = "year" :label = "year" class = "m-0 mr-2" />
            <p class = "chip-items">- Useful for Branch:</p>
            <Chip v-for="branch in productInfo.selectedBranch" :key = "branch" :label = "branch" class = "m-0 mr-2 mb-4" />
            <div class = "btn-section flex gap-2 mb-5 pt-4 border-top-1 border-400 justify-content-center">
                <Button v-if = "fromBuy || fromMyListingNotDeniedApproval" icon = "pi pi-phone" label = "Contact Seller" severity = "contrast" raised />
                <Button v-if = "fromBuy || fromMyListingNotDeniedApproval" class = "text-white" icon = "pi pi-heart" label= "Wishlist" severity = "danger" raised />
                <Button v-if = "fromBuy" label= "Buy Now!" @click = "createOrder" raised />
                <Button v-if = "fromSell" @click = "confirmListing" label = "Confirm Listing" class = "confirm-btn" raised />
                <Button v-if = "fromDeniedApproval || fromSell" label = "Edit Listing" class = "confirm-btn" @click = "editListing" />
                <Button v-if = "fromAdmin" @click = "grantApproval" label = "Grant Approval" class = "confirm-btn" raised />
                <Button v-if = "fromAdmin" @click = "denyApproval" label = "Deny Approval" severity = "danger" class = "confirm-btn text-white" raised />
            </div>
            <div class="feedback-denied-section" v-if = "showFeedbackTextArea">
                <FloatLabel>
                    <Textarea autoResize rows = "8" class = "feedback-text-area w-full" v-model="denialFeedback" required/>
                    <label for="feedback-text-area">Feedback for Denial</label>
                </FloatLabel>
                <Button @click = "sendFeedback" label = "Submit Feedback" class = "confirm-btn mt-3  mb-5 w-full" raised/>
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
import 'https://checkout.razorpay.com/v1/checkout.js';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import pageNav from '@/custom_comps/pageNav.vue';
import pageHeader from '@/custom_comps/pageHeader.vue';
import Galleria from 'primevue/galleria';
import Skeleton from 'primevue/skeleton';
import axios from 'axios'
import Textarea from 'primevue/textarea';
import FloatLabel from 'primevue/floatlabel';
import Chip from 'primevue/chip'
export default{
    data(){
        return{
            infoReached: false,
            prouductInfo: null,
            images: [],
            fromSell: false,
            fromBuy: false,
            fromMyListings: false,
            fromAdmin: false,
            fromDeniedApproval: false,
            fromMyListingNotDeniedApproval: false,
            showFeedbackTextArea: false,
            denialFeedback: '',
            existingProductId: null,
            rzp_payment_id: null,
            rzp_order_id: null,
            rzp_signature: null,
            moodleID: JSON.parse(sessionStorage.user).user.moodleID,
            phonenumber: null,
        }
    },
    components: { Textarea, FloatLabel, Chip, Toast, Skeleton, Button, pageNav, pageHeader, Galleria },
    methods: {
        //This function will be activated on 'Listing preview' when user first lists their product
        confirmListing(){
            if(this.existingProductId)
                this.updateListing()
            else
                this.uploadListing()
        },

        uploadListing(){
            axios.post("http://localhost:8000/products/upload_listing", this.productInfo) 
            .then(response => {
                this.$toast.add({ severity: 'success', summary: 'Successfully Listed', detail: `Redirecting...`, life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Settings'})}, 3000)
            })
            .catch(error => console.log("Form data could not be sent"))

        },

        updateListing(){
            axios.post("http://localhost:8000/products/update_listing", this.productInfo)
            .then(response => {
                this.$toast.add({ severity: 'success', summary: 'Successfully Updated', detail: `Redirecting...`, life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Settings'})}, 3000)
            })
            .catch(error => console.log(error))
        },

        editListing(){
            console.log("value of id when in details: ")
            console.log(this.existingProductId)
            this.$router.push({name: 'Sell', params: {
                filledValues: JSON.stringify({
                    title: this.productInfo.title,
                    category: this.productInfo.category,
                    price: this.productInfo.price,
                    productDesc: this.productInfo.productDesc,
                    selectedYear: this.productInfo.selectedYear,
                    selectedBranch: this.productInfo.selectedBranch,
                    selectedItemType: this.productInfo.selectedItemType,
                    selectedCondition: this.productInfo.selectedCondition,
                    image_urls: this.productInfo.image_urls,
                }),
                toEditListing: true,
                id: this.existingProductId,
            }
            })
        },
        //This function is activated on 'Inspect Listing' by admin if they have no problem with the listing
        grantApproval(){
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
            const feedbackJSON = {
                productId: this.$route.params.productId,
                feedback: this.denialFeedback,
            }
            axios.post("http://localhost:8000/admin_actions/send_negative_feedback", feedbackJSON)
            .then(response => {
                this.$toast.add({ severity: 'warning', summary: 'Admin Approval Denied!', detail: 'Redirecting to dashboard', life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Admin Dashboard'})}, 3000)
            })
            .catch(error => console.log(error))
        },

        createOrder(){
            const currentUser= JSON.parse(sessionStorage.user).user.moodleID
            if(this.productInfo.moodleID == currentUser)
                this.$toast.add({severity : "error", summary: 'Invalid attempt', detail : "This is your listing", life : 3000 })
            else{
                const productJSON = {
                    moodleID: currentUser,
                    productId: this.$route.params.productId,
                    product: this.productInfo
                }
                axios.post("http://localhost:8000/payments/create_order", productJSON)
                .then(response => {
                    const order_data = response.data.current_order
                    var options = {
                        "key": import.meta.env.VITE_RZP_ID, // Enter the Key ID generated from the Dashboard
                        "amount": `${order_data.amount}`, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "CampusSwap", //your business name
                        "description": `${this.productInfo.title}`,
                        "order_id": `${order_data.id}`, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (response){
                            this.rzp_order_id = response.razorpay_order_id
                            this.rzp_payment_id= response.razorpay_payment_id
                            this.rzp_signature = response.razorpay_signature
                            const payment_response = {
                                rzp_order_id: this.rzp_order_id,
                                rzp_payment_id: this.rzp_payment_id,
                                rzp_signature: this.rzp_signature,
                                buyer: currentUser,
                            }
                            axios.post("http://localhost:8000/payments/record_payment", payment_response) 
                            .then(response => console.log(response))
                            .catch(error => console.log(error))
                        },
                        "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                            "name": `${currentUser}`, //your customer's name
                            "email": `${JSON.parse(sessionStorage.user).user.email}`, 
                            "contact": `${this.phonenumber}`  //Provide the customer's phone number for better conversion rates 
                        },
                        "theme": {
                            "color": "#3399cc",
                            "backdrop_color": "#000000" 
                        },
                    };
                    const rzp1 = new Razorpay(options);
                    rzp1.open();
                })
                .catch(error => console.log(error))
            }
        },
    },

    created(){
        //getting user's phone number
        axios.get(`http://localhost:8000/apis/get_phone/${this.moodleID}`)
        .then(response => {
            this.phonenumber = response.data.phonenumber
        })
        .catch(error => console.log(error))
        //storing product info in local variable
        if(this.$route.params.id)
            this.existingProductId = this.$route.params.id
        this.productInfo = JSON.parse(this.$route.params.product)
        this.infoReached = true
        //Galleria requires a list of JSONs to display images, therefore creating this
        for(let url of this.productInfo.image_urls)
            this.images.push({itemImageSrc: url, alt: "No Image Available"})
        //Redirect from Sell
        if(this.$route.params.fromSell)
            this.fromSell = true
        //Redirect from Admin-Approval
        if(this.$route.params.fromAdmin)
            this.fromAdmin = true
        // Redirect from my-listings where admin has denied approval
        if(this.$route.params.adminStatus == 'deny')
            this.fromDeniedApproval = true
        // Redirect from my-listings where admin hasn't seen the listing yet for approval
        if((this.$route.params.adminStatus == 'true') || (this.$route.params.adminStatus == false))
            this.fromMyListingNotDeniedApproval= true
        if(this.$route.params.fromBuy)
            this.fromBuy = true
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

.product-basics{
    min-width: 640px;
}

.product-details .product-title{
    margin: 0;
    font-size: 2.5rem;
    margin-bottom: .5rem;
}

.product-details .price{
    margin: 0;
    font-size: 2rem;
    margin-bottom: .3rem;
}

.product-details .product-description{
    color: #aaa;
}

.product-details .chip-items,
.product-text-detail{
    margin: 0.8rem;
    margin-left: 0;
    font-size: 1.2rem
}

.product-details .confirm-btn{
    border-radius: 0;
}

.product-details .p-inputtextarea.p-inputtext{
    width: 80%;
}
</style>
