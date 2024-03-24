<template>
    <Card style="width: 25rem; overflow: hidden; margin-bottom: 60px; min-height: 550px">
    <template #header>
        <img alt="user header" :src="image_url" style="width: 400px; height: auto;" />
    </template>
    <template #title>{{ product.title }}</template>
    <template #subtitle>{{ product.moodleID }}</template>
    <template #content>
        {{ product.product_description }}
    </template>
    <template #footer>
        <div class="button-wrapper flex justify-content-between gap-2">
            <Button class = "w-3" icon = "pi pi-heart" severity = "danger" />
            <Button class = "check-details-btn flex-1" icon = "pi pi-chevron-right" @click = "visible = true" severity = "contrast" :label = "this.main_action" />
        </div>
    </template>
</Card>
</template>

<script>
import Button from 'primevue/button'
import Card from 'primevue/card'
    export default{
        data(){
            return{
                image_url: this.product.image_urls.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', "").split(","),
            }
        },
        props: { 
            product: Object, 
            main_action: String 
        },
        name: "itemCard",
        components: { Card, Button },
        created(){
            
        }
    }
</script>

<style>
div.p-card-body{
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
}

div.p-card-content{
    flex: 1;
    align-items: flex-end;
}
</style>