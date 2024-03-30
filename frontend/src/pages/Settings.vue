<template>
<div class="void">
    <pageHeader />
    <pageNav />
    <div class="settings-main-wrapper">
            <Panel collapsed = true class = "feature-panel" header = "Reset Password" toggleable>
                <resetPassword class = "card-items" />
            </Panel>
            <Panel collapsed = true class = "feature-panel" header = "My Listings" toggleable>
                <itemView v-for = "listing in myListings" :key = "listing.id" :product= "listing" />
            </Panel>
            <Panel collapsed = true class = "feature-panel" header = "My Resources" toggleable>
                <ResourceCard v-for = "resource in myResources" :key = "resource.id" :article = "resource" />
            </Panel>

    </div>
</div>
</template>

<script>
import Button from 'primevue/button';
import Panel from 'primevue/panel';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
import pageHeader from '@/custom_comps/pageHeader.vue';
import itemView from '@/custom_comps/itemView.vue'
import pageNav from '@/custom_comps/pageNav.vue';
import resetPassword from '@/custom_comps/resetPassword.vue';
import axios from 'axios';
import ResourceCard from '@/custom_comps/ResourceCard.vue';
export default{
    data(){
        return{
            myListings: null,
            myResources: null,
        }
    },
    components: { ResourceCard, resetPassword, Panel, pageHeader, itemView, pageNav, Button, Password, FloatLabel },
    created(){
        const moodleID = Number(JSON.parse(sessionStorage.user).user.moodleID)
        axios.get(`http://localhost:8000/products/user_listings_and_resources/${moodleID}`)
        .then(response => {
            this.myListings = response.data.listings
            this.myResources = response.data.resources
        })
        .catch(error => console.log(error))
    }
}
</script>

<style>
.settings-main-wrapper{
    background-color: #09090b;
    display: flex;
    flex-direction: column;
    justify-content: center; 
    align-items: center;
}

.p-panel.feature-panel{
    width: 70vw;
    background: #090909;
    border: .05rem solid #999;
    padding: 1.5rem 1rem;
}

.feature-panel .p-panel-title{
    letter-spacing: -.1rem;
    font-size: 1.5rem;
    text-transform: uppercase;
    font-weight: 300;
}
</style>