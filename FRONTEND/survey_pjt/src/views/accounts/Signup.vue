<template>
  <div class="h-100">
    <Nav></Nav>
    <div style="margin-left: 25vw; margin-right: 25vw; margin-top:15px">
      <div class="text-center">
        <!-- <h2 class="title_font" style="font-weight:bold; font-size:100px;">
        <v-icon class="fas fa-user-plus" color='blue' size="90"></v-icon> -->
        <img src="@/assets/초롱.jpg" width="65%" />
        <!-- </h2>  -->
      </div>
      <form action="" style="margin-top: 2vh;">
        <v-text-field v-model="signupData.username" label="USER ID" outlined required clearable></v-text-field>
        <div v-if="signupErr.overlabErr" class="mt-2">
          <v-alert dense outlined type="error">
            존재하는 아이디입니다.
          </v-alert>
        </div>
        <div v-if="signupErr.usernameErr" class="mt-2">
          <v-alert dense outlined type="error">
            아이디를 입력하세요.
          </v-alert>
        </div>
        <v-text-field v-model="signupData.email" label="EMAIL" outlined required clearable></v-text-field>
        <div v-if="signupErr.emailErr" class="mt-2">
          <v-alert dense outlined type="error">
            이메일을 입력하세요.
          </v-alert>
        </div>
        <div v-if="signupErr.emailValidErr" class="mt-2">
          <v-alert dense outlined type="error">
            유효한 이메일 주소가 아닙니다. 이메일을 다시 입력하세요.
          </v-alert>
        </div>
        <div v-if="signupErr.emailOverlabErr" class="mt-2">
          <v-alert dense outlined type="error">
            중복된 이메일입니다.
          </v-alert>
        </div>
        <v-text-field v-model="signupData.password1" label="PASSWORD" type="password" required outlined clearable></v-text-field>
        <div v-if="signupErr.password1Err" class="mt-2">
          <v-alert dense outlined type="error">
            비밀번호를 입력하세요.
          </v-alert>
        </div>
        <div v-if="signupErr.shortErr" class="mt-2">
          <v-alert dense outlined type="error">
            비밀번호가 너무 짧습니다. 최소 8자리 이상 입력하세요.
          </v-alert>
        </div>
        <div v-if="signupErr.commonErr" class="mt-2">
          <v-alert dense outlined type="error">
            비밀번호가 너무 단순합니다.
          </v-alert>
        </div>
        <v-text-field v-model="signupData.password2" label="PASSWORD Confirm" type="password" outlined clearable required></v-text-field>
        <div v-if="signupErr.password2Err" class="mt-2">
          <v-alert dense outlined type="error">
            비밀번호를 입력하세요.
          </v-alert>
        </div>
        <div v-if="signupErr.diffErr" class="mt-2">
          <v-alert dense outlined type="error">
            비밀번호가 일치하지 않습니다.
          </v-alert>
        </div>
        <div class="mt-2">
          <v-btn class="primary pull-right" @click="signup(signupData)" style="width:30%">
            <strong>회원가입 완료!</strong>
          </v-btn>
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
  name: "Signup",
  data() {
    return {
      signupData: {
        username: null,
        email: null,
        password1: null,
        password2: null,
      },
    };
  },
  methods: {
    ...mapActions(["signup"]),
  },
  computed: {
    ...mapState(["signupErr"]),
  },
  created() {
    this.signupErr.overlabErr = false;
    this.signupErr.usernameErr = false;
    this.signupErr.password1Err = false;
    this.signupErr.shortErr = false;
    this.signupErr.commonErr = false;
    this.signupErr.password2Err = false;
    this.signupErr.diffErr = false;
    this.signupErr.emailErr = false;
    this.signupErr.emailValidErr = false;
    this.signupErr.emailOverlabErr = false;
  },
};
</script>

<style scoped>
.container {
  margin-top: 100px;
}
.title_font {
  font-family: "Jua", sans-serif;
}
</style>
