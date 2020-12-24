// import Vue from 'vue'
// import Router from 'vue-router'

import RegisterPage from "@/components/pages/RegisterPage.vue";
import SearchPage from "@/components/pages/SearchPage.vue";
import DetailPage from "@/components/pages/DetailPage.vue";
import UpdatePage from "@/components/pages/UpdatePage.vue";
import DeletePage from "@/components/pages/DeletePage.vue";

// Vue.use(Router);

const routes = [{
    path: '/',
    redirect: '/Home'
}, {
    path: '/Home',
    component: SearchPage
}, {
    path: '/Register',
    component: RegisterPage
}, {
    path: '/Detail',
    component: DetailPage
}, {
    path: '/Update',
    component: UpdatePage
}, {
    path: '/Delete',
    component: DeletePage
}, {
    path: '*',
    redirect: '/'
}];

// const router = new Router({routes});

export default routes;