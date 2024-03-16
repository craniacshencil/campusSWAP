<template>
<div class="void">
    <pageHeader />
    <pageNav />
    <Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px;">
        <template #item="slotProps">
            <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%" />
        </template>
        <template #thumbnail="slotProps">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" />
        </template>
    </Galleria>
</div>

</template>

<style>
</style>

<script>
import pageNav from '@/custom_comps/pageNav.vue';
import pageHeader from '@/custom_comps/pageHeader.vue';
import Galleria from 'primevue/galleria';
export default{
    data(){
        return{
            images: [
            {itemImageSrc : "https://i.ibb.co/NjD1Y7z/1c2378de076b.png", alt: "No image"},
            { itemImageSrc :"https://i.ibb.co/hWcD8RV/745495564350.jpg", alt: 'No image'},
            { itemImageSrc :"https://i.ibb.co/X25P4MD/e46080598911.png", alt: 'No image'}]
        }
    },
    components: { pageNav, pageHeader, Galleria },
}
</script>

<style scoped>
.void{
    background-color: #09090b;
    height: 100vh;
    width: 100vw;
    
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
}
</style>
