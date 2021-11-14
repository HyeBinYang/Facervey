<template>
  <v-card class="nav-bar P-0" color="grey lighten-4" flat tile style="margin: 0;">
    <v-toolbar dense>
      <div @click="goHome" class="logo-container ml-0" style="cursor: pointer;">
        <v-toolbar-title class="logo-title font-weight:bold">
          <img src="@/assets/파란.jpg" width="100px;" />
        </v-toolbar-title>
      </div>
      <v-spacer></v-spacer>
      <strong v-show="authToken === null" @click="goLogin" class="nav-item" style="cursor: pointer; opacity: 0.8;">로그인</strong>
      <strong v-show="authToken === null" @click="goSignup" class="nav-item" style="cursor: pointer; opacity: 0.8;">회원가입</strong>
      <strong v-show="authToken !== null" @click="logout()" class="mr-5" style="cursor: pointer; opacity: 0.8;">로그아웃</strong>
    </v-toolbar>
  </v-card>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  methods: {
    ...mapActions(["logout", "createSurvey"]),
    goSignup() {
      this.$router.push({ name: "Signup" });
    },
    goLogin() {
      this.$router.push({ name: "Login" });
    },
    goCreateSurvey() {
      this.$router.push({ name: "CreateSurvey" });
    },
    goSurveyList() {
      this.$router.push({ name: "SurveyList" });
    },
    goHome() {
      this.$router.push({ name: "Main" });
    },
  },
  computed: {
    ...mapState(["authToken", "originFormData"]),
  },
};
</script>

<style>
.nav-item {
  margin: auto 10px;
  padding: 0;
}

.logo-container {
  display: flex;
  align-content: center;
  margin-left: 20px;
}

.logo-img {
  font-size: 20px;
  margin: auto 10px;
  color: purple;
}

.logo-title {
  margin: auto 0;
}
</style>
