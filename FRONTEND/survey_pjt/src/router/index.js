import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/views/Main.vue";
import Signup from "@/views/accounts/Signup.vue";
import Login from "@/views/accounts/Login.vue";
import CreateSurvey from "@/views/survey/CreateSurvey.vue";
import SurveyList from "@/views/survey/SurveyList.vue";
import EditSurvey from "@/views/survey/EditSurvey.vue";
import Student from "@/views/student/student.vue";
import Response from "@/views/survey/response.vue";
import ResponseStart from "@/views/survey/ResponseStart.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Main",
    component: Main,
  },
  {
    path: "/response",
    name: "Response",
    component: Response,
  },
  {
    path: "/response/alert",
    name: "ResponseStart",
    component: ResponseStart,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/survey/create",
    name: "CreateSurvey",
    component: CreateSurvey,
  },
  {
    path: "/survey/edit",
    name: "EditSurvey",
    component: EditSurvey,
  },
  {
    path: "/survey/list",
    name: "SurveyList",
    component: SurveyList,
  },
  {
    path: "/student",
    name: "Student",
    component: Student,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

// router.beforeEach((to, from, next) => {
//   const publicPages = ["Login", "Signup", "Main", "Response", "ResponseStart"]; // Login 안해도 됨
//   const authPages = ["Login", "Signup"]; // Login 되어있으면 안됨

//   const authRequired = !publicPages.includes(to.name); // 로그인 해야 함.
//   const unauthRequired = authPages.includes(to.name); // 로그인 해서는 안됨
//   const isLoggedIn = !!Vue.$cookies.isKey("auth-token");

//   if (unauthRequired && isLoggedIn) {
//     next();
//   }
//   authRequired && !isLoggedIn ? next({ name: "Login" }) : next();
// });

export default router;
