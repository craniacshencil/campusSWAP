<template>
    <div class="resource-form-wrapper w-full flex flex-column justify-content-center align-items-center mt-7">
        <h1 class = "resources-page-title uppercase font-light text-5xl text-center mt-9">{{ h1Title }}</h1>
        <div class = "mde-wrapper w-9 flex flex-column justify-content-center">
          <textarea ref="editor"></textarea>
        </div>
    </div>
</template>

<script>
import EasyMDE from 'easymde';
export default {
  data(){
      return{
          h1Title: "Create a Resources Catalogue",
          content: "",
      }
  },
  mounted() {
    // Initialize EasyMDE
    this.editor = new EasyMDE({
      element: this.$refs.editor,
      // Add your configurations here
    });
  },
  beforeDestroy() {
    // Destroy EasyMDE instance to prevent memory leaks
    if (this.editor) {
      this.editor.toTextArea();
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