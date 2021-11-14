import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import VueCookies from 'vue-cookies'
import store from './store'
import { mapActions, mapGetters } from "vuex"

Vue.use(VueCookies)

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),
  methods: {
    ...mapActions(["logout"])
  },
  created() {
    if (performance.navigation.type === 0 && this.isLoggedIn) {
      this.logout()
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn"])
  }
}).$mount('#app')
