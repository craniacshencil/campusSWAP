<template>
    <Toast />
    <div class="resource-form-wrapper w-full flex flex-column justify-content-center align-items-center mt-7">
        <h1 class = "resources-page-title uppercase font-light text-5xl text-center mt-9">{{ h1Title }}</h1>
        <div class = "mde-wrapper w-9 flex flex-column justify-content-center">
          <textarea ref="editor"></textarea>
        </div>
        <Button label = "Submit Resource" @click = "submitResource" class = " mb-5" />
    </div>
</template>

<script>
import EasyMDE from 'easymde';
import Button from 'primevue/button'
import Toast from 'primevue/toast'
import axios from 'axios'
export default {
    components: { Button },
    data(){
        return{
            h1Title: "Create a Resources Catalogue",
            content: "",
        }
    },
    mounted() {
        this.editor = new EasyMDE({
        element: this.$refs.editor,
        });
    },
    beforeDestroy() {
        if (this.editor) {
        this.editor.toTextArea();
        }
    },
    methods: {
        submitResource(){
            if(this.editor.value()){
                const resourceJSON = {
                    "moodleId": JSON.parse(sessionStorage.user).user.moodleID,
                    "resource": this.editor.value(),
                }
                axios.post("http://localhost:8000/products/upload_resource", resourceJSON)
                .then(response => {
                this.$toast.add({ severity: 'success', summary: 'Successfully Listed Resource', detail: 'Redirecting to user-profile...', group: 'br', life: 3000 });
                setTimeout(() => {this.$router.push({name: 'Settings'})}, 3000)
                })
                .catch(error => console.log(error))
            }

            else{
                this.$toast.add({ severity: 'error', summary: 'Empty Resource Section', detail: "You haven't filled in anything", group: 'br', life: 3000 });
            }
        }
    }
};
</script>

<style>
@import url('https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.css');

.editor-toolbar{
  height: 3rem;
  display: flex;
  justify-content: space-around;
}

.editor-toolbar button{
  flex: 1;
}

.editor-toolbar button.active{
  background: white;
  color: black;
}

.editor-toolbar button:hover{
  color: black;
}

.CodeMirror-wrap{
  background: #222;
  color: white;
}

.editor-preview-full{
  background: #222;
  color: white;
}

.CodeMirror-cursors, 
.CodeMirror-cursor{
  color: white;
  border: white 0.01rem solid;
  border-top: 0;
  border-bottom: 0;
}

.editor-toolbar.fullscreen{
  background: black;
}

.CodeMirror-fullscreen.CodeMirror-wrap,
.editor-preview-side{
  background: #222;
}

.CodeMirror-selectedtext{
  color: black; 
}
</style>