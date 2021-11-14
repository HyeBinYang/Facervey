<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  data() {
    return {
      timer: null,
      tmp: false,
    };
  },
  methods: {
    ...mapActions(['logout', 'createSurvey']),
    goSignup() {
      this.$router.push({ name: 'Signup' })
    },
    goLogin() {
      this.$router.push({ name: 'Login' })
    },
    goCreateSurvey() {
      this.$router.push({ name: 'CreateSurvey' })
    },
    goSurveyList() {
      this.$router.push({ name: 'SurveyList' })
    },
    goHome() {
      this.$router.push({ name: 'Main' })
    },
  },
  computed: {
    ...mapState(['authToken' ,'originFormData']),
  },
};
</script>

<style>
</style>
