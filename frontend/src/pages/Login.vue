<template>
    <div class="void">
        <Toast />
        <h1>Login</h1>
        <form class = "login-form">
            <div class="form-field">
                <InputGroup>
                    <InputText type = "number" v-model="moodleID" placeholder = MoodleID autofocus />
                    <InputGroupAddon>
                        <i class = "pi pi-user"></i> 
                    </InputGroupAddon>
                </InputGroup>
                <small v-if = "loginError == noExistingAccount">{{ noExistingAccount}}</small>
                <small v-if = "loginError == invalidMoodleID">{{ invalidMoodleID }}</small>
            </div>

            <div class="form-field">
                <Password v-model = passText placeholder = "Password" :feedback = false toggleMask inputStyle = "width: 30vw" required />
                <small v-if = "loginError == incorrectPassword">{{ incorrectPassword }}</small>
            </div>

            <div class = all-btns>
                <Button class = submit-btn label = Submit @click = "submitForm" />
                <div class = links>
                    <Button class = forgot-pass-btn label = "Forgot Password" link />
                    <Button class = sign-up-btn label = "Sign up" @click = toRegister link />
                </div>
            </div>
        </form>
        <div class="login-successful" v-if = "loginError == noError">
            <Message severity = "success">Login successful</Message>
            <ProgressBar mode = "indeterminate" style = "height: 0.5rem"></ProgressBar>
            <p>Redirecting to home...</p>
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
import Message from 'primevue/message'
import ProgressBar from 'primevue/progressbar'
import Toast from 'primevue/toast'
export default{
    name: "Login",
    components: { Toast, InputGroup, InputGroupAddon, Button, InputText, passField, Password, Message, ProgressBar },
    data(){
        return {
            passText: "",
            moodleID: "",
            loginError: "", 
            incorrectPassword: "Incorrect password",
            noExistingAccount: "Account does not exist for entered MoodleID",
            invalidMoodleID: "Invalid MoodleID",
            noError: "No Error",
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
            }, { withCredentials: true}).then(response => {
                this.loginError = response.data.login_error
                if(this.loginError == this.noError){
                    const user = {
                        'moodleID': response.data.moodleID,
                        'email': response.data.email,
                        'first_name': response.data.first_name,
                        'last_name': response.data.last_name
                    }
                    this.$store.commit('assignUser', user)
                    this.$store.commit('toggleIsAuthenticated', true)
                    setTimeout(() => {this.$router.push('/')}, 750)
                }
            }).catch(error => {
                console.log(error);
            });

        },
    },
    // mounted(){
    //     console.log(sessionStorage.getItem('loginWarningState'))
    //     console.log(typeof sessionStorage.getItem('loginWarningState'))
    //     if(sessionStorage.getItem('loginWarningState') === "true"){
    //         this.$toast.add({ severity: 'error', summary: "Login Required", detail: `page requires you to login`, life: 3000})
    //         sessionStorage.setItem("loginWarningState", true)
    //     }
    // }
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

small{
    display: block;
    color: rgba(255, 0, 0, 0.7);
    margin-top: 0.1rem;
}

.login-successful{
    width: 30vw;    
}

p{
    text-align: center;
    margin: 0;
    padding: 0.2rem;
}
</style>