<template>
  <div class="container mt-5">
    <form>
      <h1 class="jumbotron">Add Tasks in <span class="font-italic">{{title}}</span></h1>
      <div class="form-group">
          <input type="text" placeholder="Enter Card Title" class="form-control mt-3" v-model="card.title"/>
        <div class="form-group">
          <textarea type="text" rows="4" placeholder="Enter Card Description" class="form-control mt-3" v-model="card.description"></textarea>
        </div>
          <input type="hidden" :value="this.groupID">
          <input type="submit" class="btn btn-danger mt-3" value="Submit" @click="addTask()"/>
      </div>
    </form>
  </div>
</template>

<script>
  import axios from 'axios';
    export default {
        name: "TaskForm",
        data() {
          return {
            groupID: this.$route.params.gId,
            title: this.$route.params.gt,
            message: '',
            card: {
              title:'',
              description:'',
            }
          }
        },
        methods: {
            addTask() {
                console.log("Requesting data")
              axios.post('http://127.0.0.1:8000/api/cards/', {
                card_title: this.card.title,
                card_description: this.card.description,
                group: this.groupID,
              })
              this.$router.go('board')
            }
        }
    }
</script>

<style scoped>

</style>
