<template>
    <div class = "container flex justify-content-between gap-5">
        <div class = "image-main-info flex gap-3">
            <img class = "img-spot" alt="user header" src="@/assets/placeholder.webp" style="width: 180px; height: auto;" />
            <div class = "flex flex-column">
                <h3 class = "product-title">{{ product.title }}</h3>
                <h4 class = "product-seller">{{ product.moodleID }}</h4>
        </div>
        </div>
        <div class = "flex flex-column justify-content-between">
            <h1 class = "product-price">₹{{ product.price }}</h1>
            <div class = "flex gap-1">
                <Button icon = "pi pi-heart" severity = "danger" outlined />
                <Button class = "main-btn" icon = "pi pi-chevron-right" severity = "contrast" label = "Check details" />
            </div>
        </div>
    </div>
</template>
<script>
import Button from 'primevue/button';
export default{
    props: {product: Object}
        ,
    data(){
        return {
                moodleID: 22106025,
                // seller_name: 'John Doe',
                // title: 'vim-bindings',
                category: 'productivity',
                // price: '000',
                selectedYear: ['BE', 'TE', 'SE'],
                selectedBranch: ['CS', 'AIML', 'DS'],
                selectedItemType: ['Gadgets', 'Stationery'],
                selectedCondition: 'Brand New',
                productDesc: 'Very Useful Item',
                image_urls: ['https://i.ibb.co/RY5BtG9/443bb77060cf.png'],
                adminApproval: false,
        }
    },
    components: {Button},
}
</script>
<style scoped>
.container{
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

.main-btn{
    padding-left: .5rem;
    border-radius: .4rem;
}
</style>
