<template>
<div class="void">
    <pageHeader />
    <pageNav />
        <Panel class = "test-boi" header = "Reset Password" toggleable>
            <resetPassword />
            <!-- <div class="reset-pass-form">
            <FloatLabel>
                <Password class = "first-field reset-pass-field" v-model="oldPassword" id="oldpassword" :feedback="false" />
                <label for="oldpassword">Current Password</label>
            </FloatLabel>
            <FloatLabel>
                <Password class = "reset-pass-field" v-model="newPassword" id="newpassword" />
                <label for="newpassword">New Password</label>
            </FloatLabel>
            <FloatLabel>
                <Password class = "reset-pass-field" v-model="confirmNewPassword" id="confirmpassword" />
                <label for="confirmpassword">Confirm New Password</label>
            </FloatLabel>
            <Button class = "reset-pass-btn" severity = "contrast" raised @click = "resetPassword" label = "Submit" />
            </div> -->
        </Panel>
</div>
</template>

<script>
import Button from 'primevue/button';
import Panel from 'primevue/panel';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
import pageHeader from '@/custom_comps/pageHeader.vue';
import pageNav from '@/custom_comps/pageNav.vue';
import resetPassword from '@/custom_comps/resetPassword.vue';

export default{
    // data(){
    //     return{
    //         oldPassword: '',
    //         newPassword: '',
    //         confirmNewPassword: '',
    //     }
    // },
    components: { resetPassword, Panel, pageHeader, pageNav, Button, Password, FloatLabel }
}
</script>

<style>
.void{
    background-color: #09090b;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.p-panel.test-boi{
    width: 70%;
    background: #090909;
    border: .05rem solid #999;
    padding: 1.5rem 1rem;
}

.test-boi .p-panel-title{
    letter-spacing: -.1rem;
    font-size: 1.5rem;
    text-transform: uppercase;
    font-weight: 300;
}

/* .reset-pass-form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1.5rem;
    height: 30vh;
    margin-top: 1rem;
}

.reset-pass-btn{
    width: 25%;
    text-transform: uppercase;
    letter-spacing: -.1rem;
    border-radius: 0;
    padding: 1rem;
    margin: 0.5rem;
} */
</style>