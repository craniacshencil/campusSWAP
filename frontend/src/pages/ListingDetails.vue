<template>
<div class="void">
    <pageHeader />
    <pageNav />
    <div class="product-basics flex justify-content-around">
        <Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px"
        :showThumbnails="false" :showIndicators="true" :changeItemOnIndicatorHover="true" :showIndicatorsOnItem="inside"
        :circular="true" :showItemNavigators="true">
            <template #item="slotProps">
                <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%" />
            </template>
        </Galleria>

        <div class="product-details">
            <h1 class = "product-title">Product-Title</h1>
            <h2 class = "price">₹399</h2>
            <p>Condition of the item: Brand New</p>
            <p>Product description ksadfj;kdjfafk</p>
            <Button icon = "pi pi-phone" label = "Contact Seller" severity = "contrast" raised />
            <Button icon = "pi pi-heart" label= "Wishlist" severity = "secondary" raised />

        </div>
    </div>
</div>

</template>
<script>
import Button from 'primevue/button';
import pageNav from '@/custom_comps/pageNav.vue';
import pageHeader from '@/custom_comps/pageHeader.vue';
import Galleria from 'primevue/galleria';
export default{
    data(){
        return{
            productInfo: null,
            images: [
            { itemImageSrc : "https://i.ibb.co/NjD1Y7z/1c2378de076b.png", alt: "No image"},
            { itemImageSrc :"https://i.ibb.co/hWcD8RV/745495564350.jpg", alt: 'No image'},
            { itemImageSrc :"https://i.ibb.co/X25P4MD/e46080598911.png", alt: 'No image'}]
        }
    },
    components: { Button, pageNav, pageHeader, Galleria },
    mounted(){
        this.productInfo = this.$route.params.sellFormData
        console.log(this.productInfo)
        console.log(typeof this.productInfo)
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
    width: 100%;
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
</style>
