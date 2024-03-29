<template>
    <Card style="width: 25rem; overflow: hidden; margin-bottom: 60px;">
    <template #header>
        <img alt="user header" :src="image_urls[0]" style="width: 400px; height: auto;" />
    </template>
    <template #title>{{ product.title }}</template>
    <template #subtitle>{{ product.moodleID }}</template>
    <template #content>
        {{ product.product_description }}
    </template>
    <template #footer>
        <div class="flex gap-3 mt-1">
            <Button label="Cancel" severity="secondary" outlined class="w-full" />
            <Button label="Save" class="w-full" />
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
            image_urls: this.product.image_urls.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', "").split(","),
            }
        },
        props: { product : Object },
        name: "itemCard",
        components: { Card, Button },
    }
</script>
