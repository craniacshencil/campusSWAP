<template>
<div>
    <Toast />
    <pageHeader />
    <pageNav />
    <article class = "resource-rendered markdown-body mt-5" v-html = "rendered"></article>
    <div class="button-actions-wrapper flex flex-column align-items-center">
        <div class="btn-section mt-4 mb-5 flex justify-content-center gap-2">
            <Button v-if = "fromAdmin" @click = "grantApproval" label = "Grant Approval" class = "confirm-btn" raised />
            <Button v-if = "fromAdmin" @click = "denyApproval" label = "Deny Approval" severity = "danger" class = "confirm-btn text-white" raised />
            <Button v-if = "fromDeniedAdminStatus" @click = "toEditResource" label = "Edit Resource" severity = "warn" class = "confirm-btn" raised />
            <ToggleButton v-if = "!fromAdmin" @click = "addStar" v-model="checked" :onLabel="resourceJSON.stars + 1" :offLabel="resourceJSON.stars + 0" onIcon="pi pi-star-fill" 
            offIcon="pi pi-star" aria-label="Do you confirm" />
        </div>
        <div class="resource-feedback-denied-section mt-5 w-6 flex flex-column" v-if = "showFeedbackTextArea">
            <FloatLabel class>
                <Textarea autoResize rows = "8" class = "feedback-text-area w-full" style = "min-width: 40%" v-model="denialFeedback" required/>
                <label for="feedback-text-area">Feedback for Denial</label>
            </FloatLabel>
            <Button @click = "sendFeedback" label = "Submit Feedback" class = "confirm-btn mt-3 mb-5 w-3 align-self-center" raised/>
        </div>
    </div>
</div>
</template>

<script>
import markdownit from 'markdown-it'
import pageHeader from '@/custom_comps/pageHeader.vue'
import pageNav from '@/custom_comps/pageNav.vue'
import Button from 'primevue/button'
import ToggleButton from 'primevue/togglebutton'
import Textarea from 'primevue/textarea'
import FloatLabel from 'primevue/floatlabel'
import Toast from 'primevue/toast'
import 'github-markdown-css/github-markdown-dark.css';
import axios from 'axios'
export default{
    data(){
        return{
            rendered: null,
            showFeedbackTextArea: false,
            denialFeedback: "",
            resourceId: this.$route.params.resourceId,
            resourceJSON: null,
            fromDeniedAdminStatus: null,
            fromNotDeniedAdminStatus: null,
            fromAdmin: false,
            usersMoodleID: JSON.parse(sessionStorage.user).user.moodleID,
            checked: false,
        }
    },
    components: { pageHeader, Toast, Button, ToggleButton, pageNav, Textarea, FloatLabel },
    methods: {
        grantApproval(){
            const resourceIdJSON = {
               resourceId: this.resourceId
            }
            axios.post("http://localhost:8000/admin_actions/grant_approval_resource", resourceIdJSON)
            .then(response => {
                this.$toast.add({ severity: 'success', summary: 'Admin Approval Granted!', detail: 'Redirecting to dashboard', life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Admin Dashboard'})}, 3000)
            })
            .catch(error => console.log(error))
        },

        denyApproval(){
            this.showFeedbackTextArea = true
        },

        sendFeedback(){
            const feedbackJSON = {
                resourceId: this.resourceId,
                feedback: this.denialFeedback,
            }
            axios.post("http://localhost:8000/admin_actions/send_negative_feedback_resource", feedbackJSON)
            .then(response => {
                this.$toast.add({ severity: 'error', summary: 'Admin Approval Denied!', detail: 'Redirecting to dashboard', life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Admin Dashboard'})}, 3000)
            })
            .catch(error => console.log(error))
        },

        toEditResource(){
            this.$router.push({ name: "Resources", params: {
                article: this.resourceJSON.resource,
                resourceId: this.resourceJSON.id
            }})
        },

        addStar(){
            const addStarJSON = {
                moodleID: this.usersMoodleID,
                resourceID: this.resourceId,
            }
            axios.post("http://localhost:8000/products/add_star", addStarJSON)
            .then(response => {
                console.log(response)
            })
            .catch(error => console.log(error))
        },

    },
    created(){
        axios.get(`http://localhost:8000/products/get_resource/${this.resourceId}`)
        .then(response => {
            this.resourceJSON = response.data
            const articleMarkdown = this.resourceJSON['resource']
            const md = markdownit()
            this.rendered = md.render(articleMarkdown)
            console.log(this.resourceJSON)
        })
        .catch(error => console.log(error))

        axios.get(`http://localhost:8000/products/user_starred_resources/${this.usersMoodleID}`)
        .then(response => {
            this.usersStars = response.data.starred_resources_id
            console.log(this.usersStars)
            console.log(this.resourceId)
            if(this.usersStars.includes(Number(this.resourceId)))
                this.checked = true
            console.log(this.checked)
        })
        .catch(error => console.log(error))

        if(this.$route.params.adminStatus == 'deny')
            this.fromDeniedAdminStatus = true
        if((this.$route.params.adminStatus == 'true') || (this.$route.params.adminStatus == false))
            this.fromNotDeniedAdminStatus= true
        if(this.$route.params.fromAdmin)
            this.fromAdmin = true
    },
}
</script>

<style>
article.resource-rendered.markdown-body {
    border: .1px solid #555;
    border-radius: .5rem;
    background: #090909;
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
}

@media (max-width: 767px) {
    .markdown-body {
        padding: 15px;
    }
}

.button-actions-wrapper .p-togglebutton .p-button-icon{
    color: #f7ca00;
}
</style>