<template>
<div class="void">
    <pageHeader />
    <pageNav />
        <Panel collapsed = true class = "reset-pass-panel" header = "Reset Password" toggleable>
            <resetPassword class = "card-items" />
        </Panel>
        <Panel collapsed = true class = "reset-pass-panel" header = "My Listings" toggleable>
                <itemView v-for = "listing in myListings" :key = "listing.id" :product= "listing" />
        </Panel>
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
export default{
    data(){
        return{
            myListings: null,
        }
    },
    components: { resetPassword, Panel, pageHeader, itemView, pageNav, Button, Password, FloatLabel },
    created(){
        const moodleID = Number(JSON.parse(sessionStorage.user).user.moodleID)
        axios.get(`http://localhost:8000/products/user_listings/${moodleID}`)
        .then(response => {
            this.myListings = response.data
        })
        .catch(error => console.log(error))
    }
}
</script>

<style>
.void{
    background-color: #09090b;
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    align-items: center;
}

.p-panel.reset-pass-panel{
    width: 70vw;
    background: #090909;
    border: .05rem solid #999;
    padding: 1.5rem 1rem;
}

.reset-pass-panel .p-panel-title{
    letter-spacing: -.1rem;
    font-size: 1.5rem;
    text-transform: uppercase;
    font-weight: 300;
}
</style>