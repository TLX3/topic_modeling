<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <SelectCIKs />
      <TopicVisualization />
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

  })
};
</script>
