<template>
    <div class="resource-card-wrapper flex justify-content-between border-bottom-1 border-200 pb-4 w-full">
        <div class="text-side">
            <h2 class = "mb-1 border-bottom-1 border-300 inline-block pr-3 pt-2">{{ this.title }}</h2>
            <h4 class = "mt-2">- {{ this.article.moodleID }}</h4>
        </div>
        <div class="button-side align-self-end">
            <Button icon = "pi pi-star" severity = "warning" outlined />
            <Button class = "check-details-btn ml-1" icon = "pi pi-chevron-right" @click = "decideAction" severity = "contrast" label = "Check details" />
        </div>
    </div>    
    <Dialog v-model:visible="visible" modal header="Track Resource Status" :style="{ width: '70vw', height: '40vh' }">
        <ProgressSteps :adminApproval = "article.admin_approval" :product = "article" :productId = "article.id" entity = "Resource" />
    </Dialog>
</template>

<script>
import Button from 'primevue/button';
import ProgressSteps from '@/custom_comps/ProgressSteps.vue';
import Dialog from 'primevue/dialog';
export default{
    props: { article: Object },
    data(){
        return{
            title: "",
            visible: false,
        }
    },
    components: { Dialog, Button, ProgressSteps },
    methods: {
        decideAction(){
            if(this.$route.name == "Settings")
                this.visible = true
            else if(this.$route.name == "Approve Resource")
                this.$router.push(`/resourcedetails/${this.article.id}`)
        }
    },
    created(){
        //To Extract the title out of the entire article
        const fullArticle = this.article.resource
        const titleEndIndex = fullArticle.indexOf('\n')
        this.title = fullArticle.substring(2, titleEndIndex)
    },
}
</script>

<style scoped>

</style>
