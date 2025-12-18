# app.py
import gradio as gr

# Pump Power Calculator Function
# Power (kW) = (Flow rate * Density * 9.81 * Head) / Efficiency

def pump_power(flow_rate, density, head, efficiency):
    try:
        g = 9.81
        efficiency = efficiency / 100  # convert percentage to decimal
        power_watts = (flow_rate * density * g * head) / efficiency
        power_kw = power_watts / 1000
        return f"Pump Power: {power_kw:.3f} kW"
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("## 🧮 Pump Power Calculator")
    gr.Markdown("Enter the pump parameters to compute hydraulic power.")

    flow = gr.Number(label="Flow Rate (m³/s)")
    density = gr.Number(label="Fluid Density (kg/m³)", value=1000)
    head = gr.Number(label="Pump Head (m)")
    efficiency = gr.Number(label="Pump Efficiency (%)", value=70)

    output = gr.Textbox(label="Result")

    btn = gr.Button("Calculate Pump Power")
    btn.click(pump_power, inputs=[flow, density, head, efficiency], outputs=output)

if __name__ == "__main__":
    demo.launch()
