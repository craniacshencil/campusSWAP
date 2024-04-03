<template>
    <Card style="width: 25rem; overflow: hidden; margin-bottom: 60px; min-height: 550px">
    <template #header>
        <img alt="user header" :src="image_urls[0]" style="width: 400px; height: auto;" />
    </template>
    <template #title>{{ product.title }}</template>
    <template #subtitle>{{ product.moodleID }}</template>
    <template #content>
        {{ product.product_description }}
    </template>
    <template #footer>
        <div class="button-wrapper flex justify-content-between gap-2">
            <Button class = "w-3" icon = "pi pi-heart" severity = "danger" />
            <Button @click = "triggerAction" class = "main-action-btn flex-1" icon = "pi pi-chevron-right" severity = "contrast" :label = "this.main_action" />
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
                sessionInfo : JSON.parse(sessionStorage.user),
                selectedYear : this.product.selected_year.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', "").split(", "),
                selectedBranch : this.product.selected_branch.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', "").split(", "),
                selectedItemType : this.product.selected_item_type.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', "").split(", "),
                selectedCondition : this.product.selected_condition.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").replaceAll('"', ""),
            }
        },
        props: { 
            product: Object, 
            main_action: String 
        },
        name: "itemCard",
        components: { Card, Button },
        methods: {
            triggerAction(){
                if(this.$route.name == "Approve Listing")
                    this.inspectListing()
                else
                    this.toListing()
            },

            inspectListing(){
                this.$router.push({ name: "Listing details", params: {
                product : JSON.stringify({
                    moodleID:this.product.moodleID,
                    title:this.product.title,
                    category:this.product.category,
                    price:this.product.price,
                    productDesc:this.product.product_description,
                    selectedYear:this.selectedYear,
                    selectedBranch:this.selectedBranch,
                    selectedItemType:this.selectedItemType,
                    selectedCondition:this.selectedCondition,
                    image_urls:this.image_urls,
                }),
                fromAdmin: true,
                productId: this.product.id,
                }})
            },

            toListing(){
                this.$router.push({ name: "Listing details", params: {
                product : JSON.stringify({
                    moodleID:this.product.moodleID,
                    title:this.product.title,
                    category:this.product.category,
                    price:this.product.price,
                    productDesc:this.product.product_description,
                    selectedYear:this.selectedYear,
                    selectedBranch:this.selectedBranch,
                    selectedItemType:this.selectedItemType,
                    selectedCondition:this.selectedCondition,
                    image_urls:this.image_urls,
                }),
                fromBuy: true,
                productId: this.product.id,
                }})
            }
        },
    }
</script>

<style>
div.p-card-body{
    flex: 1;
}

div.p-card-content{
    flex: 1;
    align-items: flex-end;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
</style>