<template>
  <div>
    <v-form ref="form" v-model="valid" class='mt-5'>
      <v-text-field v-model="info.num" :rules="Rules" label="기수" required outlined clearable></v-text-field>
      <v-select
        :items="items"
        label="지역"
        :rules="Rules"
        required
        v-model="info.region"
        outlined
        clearable
      ></v-select>
      <v-text-field v-model="info.myclass" :rules="Rules" label="반" required outlined clearable></v-text-field>
      <v-text-field v-model="info.studentnum" :rules="Rules" label="학번" required outlined clearable></v-text-field>
      <v-text-field v-model="info.myname" label="이름" :rules="Rules" required outlined clearable></v-text-field>
      <div class="d-flex justify-content-end">
        <button :disabled="!valid" @click="register()" class="btn btn-success">등록</button>
      </div>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      Rules: [(v) => !!v || "입력이 필요합니다."],
      info: {
        num: null,
        region: null,
        myclass: null,
        studentnum: null,
        myname: null,
      },
      items: ["서울", "대전", "광주", "구미"],
    };
  },
  methods: {
    register() {
      this.$refs.form.validate();
      let info = {
        s_num: this.info.studentnum,
        class_num: this.info.myclass,
        name: this.info.myname,
        y_num: this.info.num,
        region: this.info.region,
      };
      this.$store.dispatch("registerStudent", info);
      this.$refs.form.reset();
    },
    reset() {
      this.$refs.form.reset();
    },
  },
};
</script>

<style></style>
