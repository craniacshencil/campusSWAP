<template>
    <div class = "product-listing-container flex justify-content-between gap-5">
        <div class = "image-main-info flex gap-3">
            <img class = "img-spot" alt="user header" 
            :src="image_url" style="width: 180px; height: auto;" />
            
            <div class = "flex flex-column">
                <h3 class = "product-title">{{ product.title }}</h3>
                <h4 class = "product-seller">{{ product.moodleID }}</h4>
        </div>
        </div>
        <div class = "flex flex-column justify-content-between">
            <h1 class = "product-price">₹{{ product.price }}</h1>
            <div class = "flex gap-1">
                <Button icon = "pi pi-heart" severity = "danger" outlined />
                <Button class = "check-details-btn" icon = "pi pi-chevron-right" @click = "visible = true" severity = "contrast" label = "Check details" />
            </div>
        </div>
    </div>
    <Dialog v-model:visible="visible" modal header="Track Listing Status" :style="{ width: '70vw', height: '20vw' }">
        <ListingProgressSteps :adminApproval = "adminApproval"/>
    </Dialog>

</template>
<script>
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import ListingProgressSteps from '@/custom_comps/ListingProgressSteps.vue';
export default{
    props: {product: Object},
    data(){
        return {
                //WatchMojo: Top 10 reasons why you should learn regex
                image_url: this.product.image_urls.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', "").split(","),
                visible: false,
                adminApproval: this.product.admin_approval,
        }
    },
    components: { Dialog, Button, ListingProgressSteps },
}
</script>
<style>
.product-listing-container{
    width: 65vw;
    padding: 2rem 0;
    border-bottom: 1px #999 solid;
}

.product-price{
    align-self: flex-end;
    margin: 0;
    padding: 0;
}

.product-title{
    padding: 0;
    margin: 0;
    margin-top: 0.4rem;
    text-transform: capitalize;
}

.product-seller{
    padding: 0;
    margin: 0;
    margin-top: 0.5rem;
    color: #bbb;
}

.img-spot{
    border-radius: 1rem;
}

.check-details-btn{
    padding-left: .5rem;
    border-radius: .4rem;
}

</style>
