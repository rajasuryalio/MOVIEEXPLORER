import { describe, it, expect, vi } from 'vitest'

import { flushPromises, mount } from '@vue/test-utils'
import ActorDetail from '../components/ActorsDetail.vue'
vi.mock('axios', () => {
  return {
    default: {
      get: vi.fn(() =>
        Promise.resolve({ data: { objects: [{ id: 1, name: 'John Doe', year: 1980 }] } }),
      ),
    },
  }
})
describe('ActorDetail', () => {
  it('renders properly', async () => {
    const wrapper = mount(ActorDetail)
    await flushPromises()
    expect(wrapper.vm.actors.length).toBe(1)
    expect(wrapper.text()).toContain('John Doe')
    expect(wrapper.text()).toContain('1980')
  })
})
