obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
obj.ParameterBlock.Radius.Value = 10.0
obj.ParameterBlock.Height.Value = 30.0
node = MaxPlus.Factory.CreateNode(obj)
mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.ClassIds.Bend)
mod.ParameterBlock.BendAngle.Value = 45.0
node.AddModifier(mod)