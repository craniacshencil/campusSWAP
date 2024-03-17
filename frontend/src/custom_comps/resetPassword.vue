<template>
    <div class="reset-pass-form">
        <FloatLabel>
            <Password class = "first-field reset-pass-field" v-model = "oldPassword" id="oldpassword" :feedback="false" />
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
    </div>
</template>

<script>
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
        }
    },
    components: { Button, Password, FloatLabel },
    methods: {
        validateForm(){
            let isValidated = true 
            const fields = [ 
                {'oldPassword':this.oldPassword},
                {'newPassword' : this.newPassword},
                {'confirmNewPassword' : this.NewPassword},
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
            console.log(this.oldPassword)
            console.log(this.confirmNewPassword)
            console.log(this.newPassword)
            const passwords =  {
                oldPassword : this.oldPassword,
                newPassword : this.newPassword, 
                confirmNewPassword : this.confirmNewPassword,
            }
            axios.post("http://localhost:8000/apis/reset_password", passwords)
            .then(response => console.log(response))
            .catch(error => console.log(error))
        }
    }
}
</script>

<style scoped>
.reset-pass-form{
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
}
</style>