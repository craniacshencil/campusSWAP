<template>
<div class="void">
    <pageHeader />
    <pageNav />
    <div class="settings-main-wrapper">
            <Panel collapsed = true class = "feature-panel" header = "My Listings" toggleable>
                <h1 v-if = "noListings" class ="empty-section">You have 0 listings</h1>
                <itemView v-else v-for = "listing in myListings" :key = "listing.id" :product= "listing" />
            </Panel>
            <Panel collapsed = true class = "feature-panel" header = "My Resources" toggleable>
                <h1 v-if = "noResources" class ="empty-section">You have 0 resources</h1>
                <ResourceCard v-else v-for = "resource in myResources" :key = "resource.id" :article = "resource" />
            </Panel>
            <Panel collapsed = true class = "feature-panel" header = "Starred Resources" toggleable>
                <h1 v-if = "noStarredResources" class ="empty-section">You haven't starred any resources</h1>
                <ResourceCard v-else v-for = "resource in myStarredResources" :key = "resource.id" :article = "resource" from = "Starred Resources" />
            </Panel>
            <Panel collapsed = true class = "feature-panel" header = "Sold Listings" toggleable>
                <h1 v-if = "noSoldListings" class ="empty-section">Your listings haven't been sold</h1>
                <itemView v-else v-for = "listing in soldListings" :key = "listing.id" :product = "listing" from = "Sold Listings" />
            </Panel>
            <Panel collapsed = true class = "feature-panel" header = "Reset Password" toggleable>
                <resetPassword class = "card-items" />
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
            myStarredResources: null,
            soldListings: [],
            noResources: false,
            noListings: false,
            noStarredResources: false,
            noSoldListings: true,
        }
    },
    components: { ResourceCard, resetPassword, Panel, pageHeader, itemView, pageNav, Button, Password, FloatLabel },
    created(){
        const moodleID = Number(JSON.parse(sessionStorage.user).user.moodleID)
        axios.get(`http://localhost:8000/products/user_listings_and_resources/${moodleID}`)
        .then(response => {
            this.myListings = response.data.listings
            this.myResources = response.data.resources
            console.log(this.myListings)
            for(const listing_key of Object.keys(this.myListings)){
                if(this.myListings[listing_key].admin_approval == "sold"){
                    this.soldListings.push(this.myListings[listing_key])
                    delete this.myListings[listing_key]
                    this.noSoldListings = false 
                }
            }
            if(Object.keys(this.myListings).length === 0)
                this.noListings = true
            if(Object.keys(this.myResources).length === 0)
                this.noResources= true
        })
        .catch(error => console.log(error))

        axios.get(`http://localhost:8000/products/user_starred_resources/${moodleID}`)
        .then(response => {
            this.myStarredResources = response.data.starred_resources
            if(Object.keys(this.myStarredResources).length === 0)
                this.noStarredResources = true
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
    margin-bottom: 10rem;
}

.p-panel.feature-panel{
    margin-top: 2rem;
    width: 70vw;
    background: #090909;
    border: 0;
    border-bottom: .05rem solid #999;
    padding: 1.5rem 1rem;
}

.feature-panel .p-panel-title,
.empty-section{
    letter-spacing: -.1rem;
    font-size: 1.5rem;
    text-transform: uppercase;
    font-weight: 300;
}

.empty-section{
    font-size: 3rem;
    color: #999;
}
</style>