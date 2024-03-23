<template>
<Toast />
<div class="void">
    <pageHeader />
    <pageNav />
    <div v-if = "infoReached" class="product-basics flex justify-content-between">
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
            <p>Product description {{ productInfo.productDesc }}</p>
            <Button icon = "pi pi-phone" label = "Contact Seller" severity = "contrast" raised />
            <Button icon = "pi pi-heart" label= "Wishlist" severity = "secondary" raised />
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
    <Button v-if = "!fromMyListings" @click = "confirmListing" label = "Confirm Listing" class = "contrast confirm-btn" raised />
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
export default{
    data(){
        return{
            infoReached: false,
            productInfo: {},
            images: [],
            fromMyListings: false,
        }
    },
    components: { Toast, Skeleton, Button, pageNav, pageHeader, Galleria },
    methods: {
        confirmListing(){
            axios.post("http://localhost:8000/products/sell_form", this.productInfo) 
            .then(response => {
                console.log("Form data has been sent")
                this.$toast.add({ severity: 'success', summary: 'Successfully Listed', detail: `Redirecting...`, life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Settings'})}, 3000)
            })
            .catch(error => console.log("Form data could not be sent"))
        }
    },
    created(){
        this.productInfo = this.$route.params
        for(let url of this.productInfo.image_urls)
            this.images.push({itemImageSrc: url, alt: "No Image Available"})
        this.infoReached = true
        //To Not dispaly 'Confirm Listing' button when you are coming here from the 'MyListings' panel from 'Settings page'
        if(this.productInfo.fromMyListing)
            this.fromMyListings = true
    }
}
</script>

<style scoped>
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
    width: 90%;
}

.product-details{
    width: 40%;
}

.product-title{
    margin: 0;
}

.price{
    margin: 0;
}

.confirm-btn{
    border-radius: 0;
}

.btn-section{
    margin-top: 5rem;
}
</style>
