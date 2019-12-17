<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <SelectCIKs @updateCIKs="updateCIKs"/>
      <v-flex>
        <v-btn v-if="selectedCIKs.length > 0" @click='getTopics' color="green" dark>Generate Topics</v-btn>
      </v-flex>
      <TopicVisualization :chartData="chartData" />
    </v-layout>
  </v-container>
</template>

<script>
  import SelectCIKs from "./SelectCIKs";
  import TopicVisualization from "./TopicVisualization";
  export default {
    name: 'Main',
    components: {
        SelectCIKs,
        TopicVisualization
    },
    data: () => ({
        selectedCIKs: [],
        chartData: []
    }),
    methods: {
        updateCIKs (CIKs) {
          this.selectedCIKs = CIKs
        },
        getTopics () {
            let url = process.env.VUE_APP_API_URL + '/get_topics?'
            this.selectedCIKs.forEach((CIK) => {
                url += `CIKs=${CIK}&`
            })
            fetch(url)
                .then(response => response.json())
                .then((data) => {
                  this.chartData = data
                })
        }
    }
  };
</script>
