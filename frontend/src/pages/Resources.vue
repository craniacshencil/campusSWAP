<template>
    <div class="void h-screen w-screen">
        <pageHeader />
        <pageNav />
        <ResourcesNav @sendDisplayInfo = "handleRequiredView" />
        <div v-if = "showCreateResources" class="create-resources">
            <p>Create resources section</p>
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
export default{
    data(){
        return{
            showFindResources: true,
            showCreateResources: false,
        }
    },
    components: { pageHeader, pageNav, ResourcesNav },
    methods: {
        handleRequiredView(mode){
            console.log(mode)
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