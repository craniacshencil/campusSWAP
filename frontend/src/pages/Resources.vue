<template>
    <div class="void h-full w-full">
        <pageHeader />
        <pageNav />
        <ResourcesNav @sendDisplayInfo = "handleRequiredView" class = "mt-4" />
        <div v-if = "showCreateResources" class="create-resources w-full flex flex-column justify-content-center">
            <MarkdownEditor :previousArticle = "previousArticle" :id = "this.$route.params.resourceId" />
        </div>
        <div v-if = "showFindResources" class="find-resources w-11 mt-5">
            <div class="resources-wrapper">
                <ResourceCard v-for = "resource in approvedResources" :key = "resource.id" :article = "resource" />
            </div>
        </div>
    </div>
</template>

<script>
import pageHeader from "@/custom_comps/pageHeader.vue";
import pageNav from "@/custom_comps/pageNav.vue";
import ResourcesNav from "@/custom_comps/ResourcesNav.vue";
import MarkdownEditor from "@/custom_comps/MarkdownEditor.vue"
import ResourceCard from "@/custom_comps/ResourceCard.vue";
import axios from "axios";
export default{
    data(){
        return{
            showFindResources: true,
            showCreateResources: false,
            previousArticle: null,
            approvedResources: null,
        }
    },
    components: { pageHeader, ResourceCard, pageNav, ResourcesNav, MarkdownEditor },
    methods: {
        handleRequiredView(mode){
            if(mode == 'find resources'){
                this.showFindResources = true
                this.showCreateResources = false
            }

            if(mode == 'create resources'){
                this.showCreateResources = true
                this.showFindResources = false
            }
        },
    },

    created(){
        if(this.$route.params.article){
            this.showCreateResources = true
            this.showFindResources = false
            this.previousArticle = this.$route.params.article
        }

        axios.get("http://localhost:8000/products/all_approved_resources")
        .then(response => {
            this.approvedResources = response.data.allApprovedResources
        })
        .catch(error => console.log(error))

    },
}
</script>

<style scoped>

</style>