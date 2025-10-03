import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ActorCard from '../components/ActorCard.vue'

describe('ActorCard', () => {
  it('renders properly', () => {
    const actor = { name: 'John Doe', year: 1980 }
    const wrapper = mount(ActorCard, { props: { actor } })
    expect(wrapper.text()).toContain('John Doe')
    expect(wrapper.text()).toContain('1980')
  })
})
