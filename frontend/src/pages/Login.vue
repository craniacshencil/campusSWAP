<template>
    <div class="void">
        <h1>Login</h1>
        <div class = "login-form">
            <div class="form-field">
                <InputGroup>
                    <InputText v-model="moodleID" placeholder = MoodleID autofocus />
                    <InputGroupAddon>
                        <i class = "pi pi-user"></i> 
                    </InputGroupAddon>
                </InputGroup>
            </div>

            <div class="form-field">
                <Password v-model = passText placeholder = "Password" :feedback = false toggleMask inputStyle = "width: 30vw" />
            </div>

            <div class = all-btns>
                <Button class = submit-btn label = Submit @click = "submitForm" />
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
import axios from 'axios'
import passField from '../custom_comps/passField.vue'
import Password from 'primevue/password'
export default{
    name: "Login",
    components: { InputGroup, InputGroupAddon, Button, InputText, passField, Password },
    data(){
        return {
            passText: "",
            moodleID: "",
        }
    },

    methods: {
        toRegister(){
            this.$router.push("/register")
        },

        submitForm(){
            axios.post('http://localhost:8000/apis/login', {
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
    height: 100vh;
    width: 100vw;
    
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.login-form{
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