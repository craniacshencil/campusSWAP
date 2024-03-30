<template>
<div>
    <Toast />
    <pageHeader />
    <article class = "resource-rendered markdown-body mt-5" v-html = "rendered"></article>
    <div class="admin-resource-actions-wrapper flex flex-column align-items-center">
        <div class="btn-section mt-4 flex justify-content-center gap-2">
            <Button @click = "grantApproval" label = "Grant Approval" class = "confirm-btn" raised />
            <Button @click = "denyApproval" label = "Deny Approval" severity = "danger" class = "confirm-btn text-white" raised />
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
import Button from 'primevue/button'
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
            resourceId: JSON.parse(this.$route.params.articleDetails).id,
        }
    },
    components: { pageHeader, Toast, Button, Textarea, FloatLabel },
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
                this.$toast.add({ severity: 'warning', summary: 'Admin Approval Denied!', detail: 'Redirecting to dashboard', life: 3000 })
                setTimeout(() => {this.$router.push({'name': 'Admin Dashboard'})}, 3000)
            })
            .catch(error => console.log(error))
        }

    },
    created(){
        const articleMarkdown = JSON.parse(this.$route.params.articleDetails).resource
        const md = markdownit()
        this.rendered = md.render(articleMarkdown)
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
</style>