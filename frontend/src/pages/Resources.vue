<template>
    <div class="void h-full w-full">
        <pageHeader />
        <pageNav />
        <ResourcesNav @sendDisplayInfo = "handleRequiredView" class = "mt-4" />
        <div v-if = "showCreateResources" class="create-resources w-full flex flex-column justify-content-center">
            <MarkdownEditor />
        </div>
        <div v-if = "showFindResources" class="find-resources">
            <p>Find resources section</p>
        </div>
    </div>
</template>

<script>
import pageHeader from "@/custom_comps/pageHeader.vue";
import pageNav from "@/custom_comps/pageNav.vue";
import ResourcesNav from "@/custom_comps/ResourcesNav.vue";
import MarkdownEditor from "@/custom_comps/MarkdownEditor.vue"
export default{
    data(){
        return{
            showFindResources: true,
            showCreateResources: false,
        }
    },
    components: { pageHeader, pageNav, ResourcesNav, MarkdownEditor },
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
}
</script>

<style scoped>

</style>