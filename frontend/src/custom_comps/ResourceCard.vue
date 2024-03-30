<template>
    <div class="resource-card-wrapper flex justify-content-between border-bottom-1 border-200 pb-4">
        <div class="text-side">
            <h2 class = "mb-1 border-bottom-1 border-300 inline-block pr-3 pt-2">{{ this.title }}</h2>
            <h4 class = "mt-2">- {{ this.article.moodleID }}</h4>
        </div>
        <div class="button-side align-self-end">
            <Button icon = "pi pi-star" severity = "warning" outlined />
            <Button class = "check-details-btn ml-1" icon = "pi pi-chevron-right" @click = "visible = true" severity = "contrast" label = "Check details" />
        </div>
    </div>    
</template>

<script>
import Button from 'primevue/button';
export default{
    props: { article: Object },
    data(){
        return{
            title: "",
        }
    },
    components: { Button, },
    created(){
        //To Extract the title out of the entire article
        const fullArticle = this.article.resource
        const titleEndIndex = fullArticle.indexOf('\n')
        this.title = fullArticle.substring(2, titleEndIndex)
    }
}
</script>

<style scoped>

</style>
