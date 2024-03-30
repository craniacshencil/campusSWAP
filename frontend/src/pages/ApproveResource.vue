<template>
    <div class="void w-full h-full">
        <pageHeader /> 
        <div class="resources-wrapper w-10">
            <ResourceCard v-for = "resource in unapprovedResources" :key = "resource.id" :article = "resource" />
        </div>
    </div>
</template>

<script>
import ResourceCard from '@/custom_comps/ResourceCard.vue'
import pageHeader from '@/custom_comps/pageHeader.vue'
import axios from 'axios'
export default{
    data(){
        return{
            unapprovedResources: null,
        }
    },
    components:{ ResourceCard, pageHeader},
    created(){
        axios.get("http://localhost:8000/admin_actions/get_unapproved_listings_and_resources")
        .then((response) => {
            this.unapprovedResources = response.data.unapproved_resources
        })
        .catch( error => console.log(error))
    }
}
</script>

<style scoped>
</style>