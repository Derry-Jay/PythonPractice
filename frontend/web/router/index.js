import Vue from 'vue'
import Router from 'vue-router'
const routerOptions = [
  { path: '/welcome', component: 'Welcome' },
  { path: '/login', component: 'Login' },
  { path: '/signup', component: 'Signup' },
  { path: '/admin', component: 'Admin' },
  { path: '/cluster', component: 'Cluster' }
//   { path: '/disease', component: 'Disease'}
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
