<template>
  <div class="h-100">
    <Nav></Nav>
    <div style="margin-left: 25vw; margin-right: 25vw; margin-top:0;">
      <div class="text-center">
        <!-- <h2 class="title_font" style="font-weight:bold; font-size:100px;"> -->
        <img src="@/assets/main_logo1.jpg" width="80%" />
        <!-- <v-icon class="fas fa-sign-in-alt" color='blue' size="90"></v-icon> -->
        <!-- </h2>  -->
      </div>
      <form action="" style="margin-top: 0.2vh;">
        <v-text-field v-model="loginData.username" label="USER NAME" outlined required clearable></v-text-field>
        <div v-if="loginErr.usernameErr && !loginErr.emailErr && !loginErr.passwordErr" class="mt-2">
          <v-alert dense outlined type="error">
            아이디를 입력하세요.
          </v-alert>
        </div>
        <v-text-field v-model="loginData.email" label="EMAIL" outlined required clearable></v-text-field>
        <div v-if="!loginErr.usernameErr && loginErr.emailErr && !loginErr.passwordErr" class="mt-2">
          <v-alert dense outlined type="error">
            이메일를 입력하세요.
          </v-alert>
        </div>
        <v-text-field v-model="loginData.password" label="PASSWORD" type="password" outlined required clearable></v-text-field>
        <div v-if="!loginErr.usernameErr && !loginErr.emailErr && loginErr.passwordErr" class="mt-2">
          <v-alert dense outlined type="error">
            비밀번호를 입력하세요.
          </v-alert>
        </div>
        <div v-if="loginErr.usernameErr && loginErr.passwordErr" class="mt-2">
          <v-alert dense outlined type="error">
            잘못된 아이디거나 잘못된 비밀번호입니다.
          </v-alert>
        </div>
        <div>
          <v-btn class="primary pull-right" @click="login(loginData)" style="width: 30%;"> <strong>접속하기!</strong></v-btn>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import Nav from "@/components/Nav.vue";

export default {
  components: {
    Nav,
  },
  name: "Login",
  data() {
    return {
      loginData: {
        username: null,
        email: null,
        password: null,
      },
    };
  },
  methods: {
    ...mapActions(["login"]),
  },
  computed: {
    ...mapState(["loginErr"]),
  },
  created() {
    this.loginErr.usernameErr = false;
    this.loginErr.emailErr = false;
    this.loginErr.passwordErr = false;
  },
};
</script>

<style></style>
