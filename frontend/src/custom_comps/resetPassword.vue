<template>
    <Toast />
    <div class="reset-pass-form">
        <FloatLabel>
            <Password class = "first-field reset-pass-field" v-model = "oldPassword" id="oldpassword" :feedback="false" toggleMask />
            <label for="oldpassword">Current Password</label>
            <small v-if = "passError == oldPassMismatch">{{ oldPassMismatch }}</small>
        </FloatLabel>
        
        <FloatLabel>
            <Password ref = "newpass" class = "reset-pass-field" v-model="newPassword" id="newpassword" toggleMask />
            <label for="newpassword">New Password</label>
            <small v-if = "passError == passwordWeak">{{ passwordWeak }}</small>
            <small v-if = "passError == passwordWeak"></small>
            <small v-if = "passError == passwordWeak">a. It should be atleast 8 characters long</small>
            <small v-if = "passError == passwordWeak">b. Should include a capital letter, special character and a number</small>
        </FloatLabel>
        <FloatLabel>
            <Password class = "reset-pass-field" v-model="confirmNewPassword" id="confirmpassword" toggleMask />
            <label for="confirmpassword">Confirm New Password</label>
            <small v-if = "passError == newPassMismatch">{{  newPassMismatch }}</small>
        </FloatLabel>
        <Button class = "reset-pass-btn" severity = "contrast" raised @click = "validateForm" label = "Submit" />
    </div>
</template>

<script>
import Toast from 'primevue/toast'
import Button from 'primevue/button';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
import axios from 'axios';

export default{
    data(){
        return{
            oldPassword: '',
            newPassword: '',
            confirmNewPassword: '',
            passError: '',
            oldPassMismatch: "This password does not match the old password",
            newPassMismatch: "Password and Confirm Password don't match",
            passwordWeak: "Password is not strong enough"
        }
    },
    components: { Button, Toast, Password, FloatLabel },
    methods: {
        validateForm(){
            let isValidated = true 
            const fields = [ 
                {'Old Password':this.oldPassword},
                {'New Password' : this.newPassword},
                {'Confirm Password' : this.confirmNewPassword},
            ]
            for(let field of fields){
                if(!Object.values(field)[0]){
                    this.$toast.add({ severity: 'error', summary: 'Empty Field', detail: `${Object.keys(field)[0]} field is empty`, life: 3000 })
                    isValidated = false
                }
            }

            if(isValidated)
                this.resetPassword();
        },
        resetPassword(){
            const moodleID = JSON.parse(sessionStorage.user).user.moodleID
            const passwords =  {
                moodleID,
                oldPassword : this.oldPassword,
                newPassword : this.newPassword, 
                confirmNewPassword : this.confirmNewPassword,
                passwordStrength: this.$refs.newpass.meter.strength,
            }
            axios.post("http://localhost:8000/apis/reset_password", passwords)
            .then(response => {
                this.passError = response.data.errorMessage
                if(this.passError == "No Error")
                    this.$toast.add({ severity: 'success', summary: 'Password Changed', detail: 'You can login with your new password', group: 'br', life: 5000});
            })
            .catch(error => console.log(error))
        }
    }
}
</script>

<style>
.reset-pass-form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1.5rem;
    height: 30vh;
    margin-top: 2rem;
}

.reset-pass-btn{
    width: 25%;
    text-transform: uppercase;
    letter-spacing: -.1rem;
    border-radius: 0;
    padding: 1rem;
    margin: 0.5rem;
}

.reset-pass-field .p-password-input{
    width: 30rem;
}
small{
    display: block;
    color: rgba(255, 0, 0, 0.7);
    margin-left: 0.8rem;
    margin-bottom: 0.3rem;
}
</style>