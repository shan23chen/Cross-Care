// @ts-nocheck
import React from 'react';
import { Card, Text, Flex, Callout, Grid } from '@tremor/react';
import {
  IoAnalyticsSharp,
  IoLanguage,
  IoMedicalOutline
} from 'react-icons/io5';

const features = [
  {
    title: 'Data',
    metric: '>1TB Text Analyzed',
    delta: 'RedPajama + Pile',
    status: 'Large-Scale Datasets',
    color: 'emerald',
    text: 'More than X trillion tokens analyzed.',
    icon: IoAnalyticsSharp
  },
  {
    title: 'Representation',
    metric: 'Co-Occurrence Patterns',
    delta: 'Demographic-Disease-Drug',
    status: 'Representational Harm',
    color: 'blue',
    text: 'Race and Gender representation across X clinical terms.',
    icon: IoLanguage
  },
  {
    title: 'Benchmarks',
    metric: 'Benchmarking Framework',
    delta: 'Subject-Relation-Object',
    status: 'Smart SRO Generation',
    color: 'amber',
    text: 'Create benchmarks and experiments that mirror the real-world.',
    icon: IoMedicalOutline
  }
];

export default function FeaturesSection() {
  return (
    <section id="features" className="py-8 md:py-12 lg:py-32">
      <div className="text-center max-w-[64rem] mx-auto">
        <h2 className="font-heading text-3xl sm:text-4xl md:text-5xl lg:text-6xl" style={{color: "white"}} >
          Features
        </h2>
        <p className="max-w-[85%] mx-auto mt-4 text-muted-foreground sm:text-lg md:text-xl" style={{color: "white"}}>
          Explore the cutting-edge features of our project, showcasing the power
          of data in understanding complex health issues.
        </p>
      </div>

      <Grid
        numItemsSm={2}
        numItemsLg={3}
        className="gap-6 mt-8 mx-auto max-w-[58rem]"
      >
        {features.map((item) => (
          <Card key={item.title}>
            <Text>{item.title}</Text>
            <Flex
              justifyContent="start"
              alignItems="baseline"
              className="space-x-3 truncate"
            >
              <Text className="text-xl font-bold">{item.metric}</Text>
            </Flex>
            <Callout
              className="mt-6"
              title={`${item.status} (${item.delta})`}
              icon={item.icon}
              color={item.color}
            >
              {item.text}
            </Callout>
          </Card>
        ))}
      </Grid>
    </section>
  );
}
