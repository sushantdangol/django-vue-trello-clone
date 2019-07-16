<template>
  <div>
    <br>
    <br>
    <div class="container mt-5">
      <div class="card">
        <div class="card-header">
         Settings
        </div>
        <div class="card-body">
          <h5 class="card-title">Delete Task</h5>
          <p class="card-text">Please be informed that this cannot be undone. Click on "Delete":</p>
          <button href="#" class="btn btn-danger" >Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
    export default {
        name: "Settings",
        data() {
          return {
            setId: this.$route.params.id
          }
        },
        methods: {
        }
    }
</script>

<style scoped>

</style>
