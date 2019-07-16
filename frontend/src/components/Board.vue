 <template>
<div class="board mt-5">
      <!--- Components -->
    <Group />
<div>
        <button type="button" id="create-btn" class="mt-4 ml-4 fixed-bottom mb-5" data-toggle="modal" data-target="#exampleModal">
            + Create New Group
        </button>
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Create a New Group</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
              <form @submit="createGroup()">
                <input class="form-control" type="text" v-model="group.title" placeholder="Enter Group Title"/>
                <input class="btn btn-primary mt-2 float-right"  type="submit" value="Submit">
              </form>
            </div>
            </div>
        </div>
        </div>
  </div>
</div>
</template>

<script>
import Group from '../components/Other/Group'
import axios from 'axios'

export default {
    name: 'Board',
    components: {
        Group
    },
    data() {
      return {
        group: {
          title: ''
        }
      }
    },
    methods: {
      createGroup() {
        axios.post('http://localhost:8000/api/groups/', {
          group_title: this.group.title
        })
      }
    },
}
</script>

<style scoped>

  .board{
    width: 100%;
    padding: 20px;
  }

  #create-btn{
    background-color: rgba(0,0,0,0.1);
    background-repeat:no-repeat;
    padding: 10px;
    border: 1.2px solid black;
    cursor:pointer;
    overflow: hidden;
    outline:none;
    text-align: left;
    width: 300px;
  }

</style>
