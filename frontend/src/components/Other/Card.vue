<template>
    <div class="task-card">
      <br>
      <div v-for="(x, key) in this.inData" :key=key>
        <div v-if="x.pk==fromId">
          <h1 class="jumbotron">
            {{x.card_title}}
            <br>
            <br>
            <div>
              <h3>Task Description</h3>
              <p class="font-italic">{{x.card_description}}</p>
            </div>
          </h1>
          <div class="container">
            <li class="list-group-item active bg-danger">
              Add Todo
              <span>
                <form @submit="addTodo()">
                  <input class="form-control mt-1" type="text" placeholder="Type and Press Enter" v-model="todos.name">
                  <input type="hidden" :value="fromId">
                </form>
              </span>
            </li>
            <div v-for="(t, key) in todo" :key=key>
                <div v-if="t.card==x.pk">
                  <ul class="list-group">
                    <li class="list-group-item bg-dark text-white">
                      <span class="float-left">{{t.todo_name}}</span>
                      <span v-if="t.todo_status">
                        <span class="float-right bg-success p-1">Completed</span>
                      </span>
                      <span v-else>
                         <span class="float-right bg-success p-1" @click="complete(t.pk)">Mark as Completed</span>
                      </span>
                    </li>
                  </ul>
                </div>
            </div>
          </div>
        </div>
      </div>
      <router-link :to="{path: `/settings/${fromId}`}"><button class="btn btn-warning fixed-bottom mb-4 float-left ml-4">Settings</button></router-link>
    </div>
</template>

<script>
  import axios from 'axios';

    export default {
        name: "Card",
        data() {
          return {
            inData: null,
            todo: null,
            todos: {
              name:'',
            },
            fromId: this.$route.params.id,
            status: false
          }
        },
        created() {
          axios.all([this.getCard(), this.getTodo()])
            .then(axios.spread((res, response) => {
                this.inData = res.data;
                this.todo = response.data;
            }));
        },

        methods: {
          getCard() {
            return axios.get('http://127.0.0.1:8000/api/cards/?format=json')
          },
          getTodo() {
            return axios.get('http://localhost:8000/api/todos/?format=json')
          },
          addTodo() {
            axios.post('http://localhost:8000/api/todos/', {
              todo_name:this.todos.name,
              card: this.fromId
            })
            this.$router.go('card')
          },
          complete(pk) {
            axios.put(`http://localhost:8000/api/todos/${pk}/`, {
              todo_status: true
            })
            this.$router.go()
          }

        }

    }
</script>

<style scoped>

</style>
