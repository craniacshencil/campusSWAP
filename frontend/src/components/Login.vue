<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
   <div class="void">
        <h1>Login</h1>
        <div class = "register-form">
            <InputGroup>
                <InputGroupAddon>
                    <i class = "pi pi-user"></i> 
                </InputGroupAddon>
                <InputText v-model="moodleID" placeholder = MoodleID autofocus />
            </InputGroup>

            <InputGroup>
                <InputGroupAddon>
                    <i class = "pi pi-lock"></i>
                </InputGroupAddon>
                <InputText v-show = "!this.isPasswordVisible" type = password v-model = "passText" placeholder = Password ref = "passfield" />
                <Button v-show = "!this.isPasswordVisible" @click = togglePassword icon class = "pi pi-eye" />
                <InputText v-show = "this.isPasswordVisible" type = text v-model = "passText" placeholder = Password ref = "passfield" />
                <Button v-show = "this.isPasswordVisible" @click = togglePassword icon class = "pi pi-eye-slash" />
            </InputGroup>
            <div class = all-btns>
                <Button class = submit-btn label = Submit @click = "validateForm" />
                <div class = links>
                    <Button class = forgot-pass-btn label = "Forgot Password" link />
                    <Button class = sign-up-btn label = "Sign up" @click = toRegister link />
                </div>
            </div>
        </div>
   </div> 
</template>

<script>
import InputGroup from 'primevue/inputgroup'
import InputGroupAddon from 'primevue/inputgroupaddon'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import axios from 'axios'

export default{
    name: "Login",
    components: { InputGroup, InputGroupAddon,  Button, InputText, Password },
    data(){
        return {
            isPasswordVisible: false,
            passText: "",
            moodleID: "",
        }
    },

    methods: {
        togglePassword(){
            this.isPasswordVisible = !this.isPasswordVisible
        },

        toRegister(){
            this.$router.push("/register")
        },

        submitForm(){
            axios.post('ENTER_DJANGO_SERVER_ADDRESS_HERE', {
                moodleID: this.moodleID,
                passText: this.passText,
            }).then(response => {
                console.log(response);
            }).catch(error => {
                console.log(error);
            });
        },
    }

}
</script>

<style scoped>
.void{
    background-color: #09090b;
    height: 100%;
    width: 100%;
    
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.password-visibility{
    margin: 0;
    padding: 0;
}

.register-form{
    padding: 50px 10px;
    border: 0.5px solid #ddd;
    border-radius: 10px;

    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.submit-btn{
    margin-bottom: 0.5 rem;
    width: 100%;
}

.links{
    display: flex;
    justify-content: space-between;
}
</style>
