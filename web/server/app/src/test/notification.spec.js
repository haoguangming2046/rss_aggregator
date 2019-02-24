import { mount } from "@vue/test-utils";
import expect from "expect";

import Notification from "../components/Notification.vue";

const wrapper = mount(Notification);

describe("Notification.vue", () => {
	it("displays the error message corectly", () => {
		const div = wrapper.find(".alert");
		expect(div.text()).toBe("Unknown Error Occured");
	});
});
