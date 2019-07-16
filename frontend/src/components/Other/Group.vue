<template>
    <div class="group float-left">
      <div class="container-fluid">
        <div class="row flex-row flex-nowrap">
            <div v-for="(x, key) in this.grp" :key=key>
              <div class="col-3">
                 <div class="card ml-3" style="width: 18rem;">
                    <div class="card-body">
                      <h5 class="card-title">{{ x.group_title }}</h5>
                      <div v-for="(y, key) in card" :key=key>
                        <div v-if="x.pk == y.group" >
                           <div class="card bg-dark text-white mb-3" style="width: 15rem;">
                              <div class="card-body">
                                <h5 class="card-title" v-on:click="goTo(y.pk)">{{y.card_title}}</h5>
                                <p class="card-text font-italic">{{ y.card_description }}</p>
                              </div>
                           </div>
                        </div>
                      </div>
                      <router-link to="/taskform"><button type="button" v-on:click="addTask(x.pk, x.group_title)" class="btn btn-outline-danger my-2 my-sm-0 mt-4" >
                            Add Tasks
                      </button>
                      </router-link>
                    </div>
                 </div>
              </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  import axios from 'axios';
  import Card from './Card'

export default {
    name: 'Group',
    data() {
      return {
        grp: null,
        card: null
      }
    },

    created() {
      // axios.get('http://localhost:8000/api/groups/?format=json')
      //   .then(res => (this.grp=res.data))
      //   .catch(err => (console.log(err)));

        axios.all([this.getCard(), this.getGroup()])
          .then(axios.spread((response, res) => {
              this.grp =  res.data;
              this.card = response.data;
          })).catch(err => (console.log(err)))
    },

    methods: {
      addTask(groupId, title) {
        var groupID=groupId
        var titles = title
        this.$router.push({name: 'taskform', params:{gId:groupID, gt:titles}})
        // console.log("Done.")
      },

       goTo(card) {
        var cardId  = card
        this.$router.push({path:`/card/${cardId}`})
      },

      getCard() {
        return axios.get('http://127.0.0.1:8000/api/cards/?format=json')
      },

      getGroup() {
        return axios.get('http://127.0.0.1:8000/api/groups/?format=json')
      },

    }
}
</script>

<style scoped>
  #create-btn{
    background-color: rgba(0,0,0,0.1);
    background-repeat:no-repeat;
    padding: 10px;
    border: 1.2px solid black;
    cursor:pointer;
    overflow: hidden;
    outline:none;
    text-align: left;
  }
</style>
