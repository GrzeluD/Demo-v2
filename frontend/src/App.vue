<template>
  <div>
    <input type="file" @change="handleFileChange">
    <button @click="submitImage">Wyślij</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    submitImage() {
      if (!this.selectedFile) {
        console.error('No file selected');
        return;
      }

      const formData = new FormData();
      formData.append('image', this.selectedFile);

      fetch('/api/endpoint', {
        method: 'POST',
        body: formData,
      })
          .then(response => response.json())
          .then(result => {
            console.log(result);
          })
          .catch(error => {
            console.error(error);
          });
    },
  },
};
</script>
