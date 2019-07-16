import Vue from 'vue'
import Router from 'vue-router'
import Group from './components/Other/Group'
import TaskForm from './components/ui/TaskForm'
import Card from './components/Other/Card'
import Board from './components/Board'
import Settings from './components/ui/Settings'

Vue.use(Router);

export default new Router ({
  routes: [
    {
      path: '/card/:id',
      name:'card',
      component: Card
    },
    {
      path: '/',
      name: 'home',
      component: Board,
    },
    {
      path:'/taskform',
      name:'taskform',
      component: TaskForm

    },
    {
      path: '/group',
      name: 'group',
      component: Group
    },
    {
      path: '/settings/:id',
      name: 'settings',
      component: Settings
    }
  ]
})

